from typing import Any
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import CurrentUser, Pdf
from django.views.generic import CreateView
from .forms import PdfForm

# Create your views here.


class CurrentUserCreateListView(CreateView):
    """View for creating an user and a list of existing users"""
    model = CurrentUser
    template_name = "index.html"
    fields = ["username", "email", "sent_mails", "is_active", "activity_time"]
    success_url = "/"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = CurrentUser.objects.all()
        return context


def currentuser_delete(request, id):
    """view to delete an existing user"""
    if request.method == "DELETE":
        user = CurrentUser.objects.get(id=id)
        user.delete()
        return JsonResponse({"status": "Success"})


def CurrentUserUpdateApiView(request, id):
    """view to update existing user"""
    if request.method == "POST":
        user = CurrentUser.objects.get(id=id)
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.sent_mails = request.POST["sent_mails"]
        user.is_active = request.POST["is_active"]
        user.activity_time = request.POST["activity_time"]
        user.save()
    return redirect("/")


class PDFCreateListView(CreateView):
    """Create a Pdf and get list of all Pdf"""
    model = Pdf
    template_name = "pdf.html"
    form_class = PdfForm
    success_url = "/pdfs"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["pdfs"] = Pdf.objects.all()
        print(context)
        return context


def delete_pdf(request, id):
    """view to delete a pdf"""
    if request.method == "DELETE":
        pdf = Pdf.objects.get(id=id)
        pdf.delete()
        return JsonResponse({"status": "Success"})
