from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        alunos = {'id':1, 'nome_do_aluno': 'clara'}
        return JsonResponse(alunos)

