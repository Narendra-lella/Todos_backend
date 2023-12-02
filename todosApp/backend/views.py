from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Totomodel
from .serializers import TodoSerializer
from rest_framework import generics,status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
def todos(request):
    return HttpResponse("Hello World")

class TodoAPIViewSet(viewsets.ModelViewSet):
    queryset = Totomodel.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        tittle = request.GET.get('tittle')
        discription = request.GET.get('discription')
        queryset = Totomodel.objects.all()
        serializer = TodoSerializer(queryset, many=True)

        try:

            if tittle:
                print('Get 1')
                queryset = Totomodel.objects.filter(tittle=tittle)
                serializer = TodoSerializer(queryset, many=True)
                return Response(serializer.data)

            return Response(serializer.data)

        except Exception as e:
            print('Exception', e)
            return Response({'error in Get'}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self,request,*args, **kwargs):
        try:
            print('post try')
            tittle = request.data.get('tittle')
            discription = request.data.get('discription')
            
            todoform = Totomodel(
                tittle = tittle,
                discription = discription
            )
            if todoform:
                print("post 1")
                todoform.save()
            return Response({
            "success": "Successfully Submitted"})

        except Exception as e:
            print("Exception",e)
            return Response({'exception in POST'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,*args, **kwargs):
        tittle = request.query_params.get('tittle')
        discription = request.query_params.get('discription')
        is_done = request.query_params.get('is_done')
        new_tittle = request.query_params.get('new_tittle')

        try:

            instanceupdate = Totomodel.objects.all()
            if tittle:
                queryset = Totomodel.objects.filter(tittle=tittle)
                print('queryset',queryset)

                if len(queryset)!=0:
                    print('insatance',instanceupdate)
                    if tittle and discription is None:
                        print('put 1')
                        instanceupdate =  instanceupdate.filter(tittle=tittle).first()
                        instanceupdate.tittle = new_tittle
                        instanceupdate.save()
                        return Response({"success" : "Response Updated"})
                    elif tittle and discription:
                        print('put 1.1')
                        instanceupdate =  instanceupdate.filter(tittle=tittle).first()
                        instanceupdate.tittle = tittle
                        instanceupdate.discription = discription
                        instanceupdate.save()
                        return Response({"success" : "Response Updated"})
                    elif tittle and is_done in ['true']:
                        print('put 2')
                        instanceupdate = instanceupdate.filter(tittle=tittle).first()
                        instanceupdate.is_done = True
                        instanceupdate.save()
                        return Response({"success" : "Response Updated"})
                    elif tittle and is_done in ['false']:
                        print('put 3')
                        instanceupdate = instanceupdate.filter(tittle=tittle).first()
                        instanceupdate.is_done = False
                        instanceupdate.save()
                        return Response({"success" : "Response Updated"})
                else:
                    print("else")
                    return Response({'bad request'},status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Exception",e)
            return Response({"error in updation"},status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, *args, **kwargs):
        tittle = request.query_params.get('tittle')

        instancedelete = Totomodel.objects.all()
        if tittle:
            print("delete 1")
            instancedelete = instancedelete.filter(tittle=tittle).first()
            print(instancedelete)
            instancedelete.delete()
            return Response({"success" : "Response Deleted"},status.HTTP_200_OK)
        else:
            print(" error in delete")
            return Response({'error in delete'},status.HTTP_400_BAD_REQUEST)
