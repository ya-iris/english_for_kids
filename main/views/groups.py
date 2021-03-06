from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .all_students import group_check
from ..forms import EditGroupForm, CreateGroupForm
from ..models import StudentGroup, Student


@user_passes_test(group_check)
@login_required
def all_groups(request):
    """
    Renders the all_groups page, with a list of all existing groups and form for creating a new group.
    """
    groups_list = [dict(id=s_group.id, year=s_group.year, name=s_group.name,
                        student_count=len(Student.objects.filter(student_group_id=s_group.id))) for s_group in
                   StudentGroup.objects.all()]

    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'The group has been created successfully')
            return redirect('groups')
        else:
            messages.error(request, 'Please, fill the form correctly')
    else:
        create_form = CreateGroupForm()

    context = {
        'create_form': create_form
    }

    return render(request, 'main/all_groups.html', {'groups': groups_list, 'create_form': context['create_form']})


@user_passes_test(group_check)
@login_required
def group_students(request, g_id):
    """
    Renders the groups_students page, with a list of all students who belong to this group.
    Args: g_id: the id of the group being viewed.
    """
    try:
        group_obj = StudentGroup.objects.get(id=g_id)
        num = 0
        students_list = []
        for s in Student.objects.filter(student_group_id=g_id).select_related('user').values('user_id',
                                                                                             'user__last_name',
                                                                                             'user__first_name'):
            num += 1
            students_list.append(dict(num=num,
                                      id=s['user_id'], first_name=s['user__first_name'],
                                      last_name=s['user__last_name']))

        return render(request, 'main/group_students.html', {'group': group_obj, 'students': students_list})
    except ObjectDoesNotExist:
        return HttpResponse("This group could not be found")


@user_passes_test(group_check)
@login_required
def choose_student(request):
    """
    Returns list of data for all existing students.
    """
    students = [dict(
        user_id=s['user_id'], user__last_name=s['user__last_name'],
        user__first_name=s['user__first_name'], student_group_id=s['student_group_id'], student_group="")
        for s in Student.objects.all().select_related('user').values('user_id', 'user__last_name',
                                                                     'user__first_name', 'student_group_id')]
    for s in students:
        if s['student_group_id'] is None:
            s['student_group'] = "No group"
        else:
            s['student_group'] = '%s%s' % (StudentGroup.objects.get(id=s['student_group_id']).year,
                                           StudentGroup.objects.get(id=s['student_group_id']).name)

    return HttpResponse(students, content_type="application/json")


@user_passes_test(group_check)
@login_required
def add_student_to_group(request, g_id, s_id):
    """
    Sets the currently viewed group as a group of the chosen student.
    Redirects to the group_students page with list of all students.
    Args: g_id: the id of the group being viewed.
          s_id: the id of the chosen student.
    """
    student = Student.objects.get(user_id=s_id)
    student.student_group_id = g_id
    messages.success(request, "The student has been added to this group")
    student.save()
    return redirect('group_students', g_id=g_id)


@user_passes_test(group_check)
@login_required
def group(request, g_id):
    """
    Renders a single group page, with data of that group object and form for creating a new group.
    Args: g_id: the id of the group being viewed.
    """
    try:
        group_obj = StudentGroup.objects.get(id=g_id)
        student_count = len(Student.objects.filter(student_group_id=g_id))

        if request.method == 'POST':
            edit_form = EditGroupForm(request.POST, instance=group_obj)

            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, "You have updated a group successfully")
                return redirect('groups')
            else:
                messages.error(request, "You have filled the form incorrectly")
        else:
            edit_form = EditGroupForm(instance=group_obj)

        context = {
            'edit_form': edit_form,
            'group': group_obj
        }

        return render(request, 'main/group.html', {'group': context['group'], 'student_count': student_count,
                                                   'edit_form': context['edit_form']})
    except ObjectDoesNotExist:
        return HttpResponse("This group could not be found")


@user_passes_test(group_check)
@login_required
def delete_group(request, g_id):
    """
    Deletes the currently viewed group.
    Args: g_id: the id of the group being viewed.
    """
    group_object = StudentGroup.objects.get(id=g_id)
    group_object.delete()
    messages.success(request, "You have deleted a group successfully")
    return redirect('groups')


@user_passes_test(group_check)
@login_required
def delete_student_from_group(request, g_id, s_id):
    """
    Deletes the currently viewed group's id from a chosen student object student_group field.
    Args: g_id: the id of the group being viewed.
          s_id: the id of the chosen student.
    """
    student = Student.objects.get(user_id=s_id)
    student.student_group_id = None
    messages.success(request, "The student has been removed from group")
    student.save()
    return redirect('group_students', g_id=g_id)
