from django.shortcuts import render, redirect, get_object_or_404

from .models import Document
from .forms import DocumentForm
from .csv_reader import import_data


def upload_db(request):
    """Upload a database's file"""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_list_db')
    else:
        form = DocumentForm()
    return render(request, 'import_db/index.html', {
        'form': form
    })


def get_db(request):
    """Get list of available databases"""
    documents = Document.objects.all()
    return render(request, 'import_db/get_list_db.html', {'documents': documents})


def read_data(request, db_id):
    """View the exact database by id"""
    database = get_object_or_404(Document, pk=db_id)
    import_data(str(database.document), database.id)
    return render(request, 'import_db/read_data.html', {'database': database})
