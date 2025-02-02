from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from .forms import FAQForm
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """Wrap the API response in a creative JSON structure."""
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "total_faqs": len(response.data),
            "data": response.data
        })
def add_faq(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Debugging
            faq = FAQ.objects.create(answer=form.cleaned_data["answer"])
            print(f"FAQ added: {faq}")  # Debugging
            return redirect("faq_list")
        else:
            print("Form errors:", form.errors)  # Debugging

    else:
        form = FAQForm()

    return render(request, "faq/add_faq.html", {"form": form})
