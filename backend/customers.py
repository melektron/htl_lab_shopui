#!/var/www/test/.venv/bin/cgi_venv_launch

import datetime
import pydantic
import sqlmodel


class Customer(sqlmodel.SQLModel, table=True):
    model_config = pydantic.ConfigDict(
        extra="forbid"
    )
    customer_id: int = sqlmodel.Field(primary_key=True)
    title: str
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime | None
    street: str
    postal_code: int
    city: str
    email: pydantic.EmailStr | None

CustomerList = pydantic.TypeAdapter(list[Customer])


if __name__ == "__main__":
    # connect to DB
    engine = sqlmodel.create_engine("mysql+pymysql://admin:password@localhost/shop?charset=utf8mb4")  
    # create table if they don't exist yet
    sqlmodel.SQLModel.metadata.create_all(engine)

    customers: list[Customer]
    # read all customers
    with sqlmodel.Session(engine) as s:
        customers = list(s.exec(sqlmodel.select(Customer)))
    
    # return from endpoint
    print("Content-Type: text/json")
    print()
    print(CustomerList.dump_json(customers).decode())
    
