<!--
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 17:22

Overview of all customers in the Database displayed in a table
-->

<script setup lang="ts">
import { onMounted, ref } from 'vue';

const customers = ref();

onMounted(() => {
    customers.value = [
        {
            name: "Hello",
            country: "Austria",
            repr: "MyRep",
            company: "ELEKTRON"
        },
        {
            name: "Hello",
            country: "Austria",
            repr: "MyRep",
            company: "ELEKTRON"
        },
        {
            name: "Hello",
            country: "Austria",
            repr: "MyRep",
            company: "ELEKTRON"
        },
    ]
});

</script>

<template>
    <div>
        <Fieldset legend="List of customers">
            <DataTable :value="customers" class="min-h-auto">
                <Column field="name" header="Name"></Column>
                <Column field="country" header="Country"></Column>
                <Column field="repr" header="Representative"></Column>
                <Column field="company" header="Company"></Column>
            </DataTable>
        </Fieldset>
    </div>
</template>

<style>
@media (min-width: 1024px) {
    .about {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }
}
</style>