/*
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 23:14

Functions for accessing the customers API
*/

export interface Customer {
    customer_id: number
    title: string
    first_name: string
    last_name: string
    date_of_birth: Date | null
    street: string
    postal_code: number
    city: string
    email: string | null
}

export async function fetchAllCustomers(): Promise<Customer[]> {
    // for now, we simply fetch this right from  ignore validation and just return the stuff straight away
    let data = await (await (await fetch("/api/customers.py")).json()) as Customer[];
    // we know for certain that the data is in wrong format so we parse that
    data.map(c => {
        if (c.date_of_birth !== null) {
            // at this point c.date_of_birth is probably a date string, so now we create a date object
            c.date_of_birth = new Date(c.date_of_birth)
        }
    })
    console.log(data);
    return data;
}