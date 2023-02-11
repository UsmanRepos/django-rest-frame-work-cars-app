from django.core.paginator import Paginator
from rest_framework import status, views
from rest_framework.response import Response
from .models import Car, CarPlan
from .serializers import CarSerializer, CarPlanSerializer

class CarAPIView(views.APIView):
    def get_car(self, id):
        try:
            car = Car.objects.get(pk=id)
            return car
        except Car.DoesNotExist:
            pass
        
    def get_car_plan(self, id):
        try:
            car = CarPlan.objects.get(pk=id)
            return car
        except CarPlan.DoesNotExist:
            pass

    def get(self, request):
        persons = Car.objects.all()
        page = request.GET.get('page', 1)
        page_size = 10
        paginator = Paginator(persons, page_size)  

        serializer = CarSerializer(paginator.page(page), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        plan = self.get_car_plan(data.pop('plan'))
        data['plan'] = plan.__dict__

        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data=request.data
        car = self.get_car(id=data.get('id'))
        plan = self.get_car_plan(data.pop('plan'))
        data['plan'] = plan.__dict__

        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data=request.data
        car = self.get_car(id=data.get('id'))
        plan = self.get_car_plan(data.pop('plan'))
        data['plan'] = plan.__dict__

        serializer = CarSerializer(car, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        person = self.get_car(id=request.data.get('id'))
        person.delete()
        return Response({"message": "Record is deleted from the database"},status=status.HTTP_204_NO_CONTENT)

    # def get(self, request, *args, **kwargs):
    #     cars = Car.objects.all()
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     plan = data.pop('plan')
    #     car = Car.objects.create (
    #         brand = data['brand'],
    #         model = data['model'],
    #         production_year = data['production_year'],
    #         engine_type = data['engine_type'],
    #         car_body = data['car_body']
    #     )
    #     car.save()
    #     car.plan = CarPlan.objects.get(pk=plan)

    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def put(self, request, *args, **kwargs):
    #     data = request.data
    #     car = Car.objects.get(pk=data.get('id'))
    #     plan = data.pop('plan')

    #     car.brand = data['brand']
    #     car.model = data['model']
    #     car.production_year = data['production_year']
    #     car.engine_type = data['engine_type']
    #     car.car_body = data['car_body']
    #     car.plan = CarPlan.objects.get(pk=plan)
    #     car.save()

    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request, *args, **kwargs):
    #     data = request.data
    #     car = Car.objects.get(pk=data.get('id'))
    #     plan = data.get('plan')

    #     car.brand = data.get('brand', car.brand)
    #     car.model = data.get('model', car.model)
    #     car.production_year = data.get('production_year', car.production_year)
    #     car.engine_type = data.get('engine_type', car.engine_type)
    #     car.car_body = data.get('car_body', car.car_body)
    #     car.plan = CarPlan.objects.get(pk=plan)
    #     car.save()

    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request, *args, **kwargs):
    #     car = Car.objects.get(request.data.get('id'))
    #     car.delete()
        # return Response({"message": "Record is deleted from the database"}, status=status.HTTP_204_NO_CONTENT)




