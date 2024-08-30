from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Document

# View Document
@permission_required('bookshelf.can_view', raise_exception=True)
def view_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'bookshelf/view_document.html', {'document': document})

# Create Document
@permission_required('bookshelf.can_create', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        # Handle document creation logic here
        return redirect('book_list')
    return render(request, 'bookshelf/create_document.html')

# Edit Document
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        # Handle document editing logic here
        return redirect('book_list')
    return render(request, 'bookshelf/edit_document.html', {'document': document})

# Delete Document
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_document.html', {'document': document})

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publish_date = form.cleaned_data['publish_date']
            # (e.g., save to the database)
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

