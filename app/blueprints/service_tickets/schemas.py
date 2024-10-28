from  app.models import Service_tickets
from app.extensions import ma


# class CustomersSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Customers

class Service_ticketsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service_tickets


# customer_schema = CustomersSchema()
# customers_schema = CustomersSchema(many=True)

service_ticket_schema = Service_ticketsSchema()
service_tickets_schema = Service_ticketsSchema(many=True)