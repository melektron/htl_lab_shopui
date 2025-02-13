#!/var/www/test/.venv/bin/cgi_venv_launch

import csv
import datetime
import typing
import pydantic
import sqlmodel


class Customer(sqlmodel.SQLModel, table=True):
    model_config = pydantic.ConfigDict(
        extra="forbid"
    )
    customer_id: int                        = sqlmodel.Field(schema_extra={"validation_alias": "Nr."}, primary_key=True)
    title: str                              = sqlmodel.Field(schema_extra={"validation_alias":"Anrede"})
    first_name: str                         = sqlmodel.Field(schema_extra={"validation_alias":"Vorname"})
    last_name: str                          = sqlmodel.Field(schema_extra={"validation_alias":"Nachname"})
    date_of_birth: datetime.datetime | None = sqlmodel.Field(schema_extra={"validation_alias":"Geburtsdatum"})
    street: str                             = sqlmodel.Field(schema_extra={"validation_alias":"Straße"})
    postal_code: int                        = sqlmodel.Field(schema_extra={"validation_alias":"Postleitzahl"})
    city: str                               = sqlmodel.Field(schema_extra={"validation_alias":"Stadt"})
    email: pydantic.EmailStr | None         = sqlmodel.Field(schema_extra={"validation_alias":"EMail"})

    @pydantic.field_validator("date_of_birth", mode="before")
    @classmethod
    def validate_dob(cls, v: typing.Any) -> datetime.datetime:
        if not v:
            return None
        return datetime.datetime.strptime(v, "%d.%m.%Y")
    
    @pydantic.field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, v: typing.Any) -> datetime.datetime:
        if not v:
            return None
        return v


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
    
