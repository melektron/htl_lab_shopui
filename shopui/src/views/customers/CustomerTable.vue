<!--
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 17:22

Overview of all customers in the Database displayed in a table
-->

<script setup lang="ts">
import { onMounted, ref, useTemplateRef } from 'vue';
import { fetchAllCustomers } from '@/api';
import type { Customer } from '@/api';
import { onKeyStroke } from "@vueuse/core";
import type { DataTableFilterMeta, DataTableFilterMetaData, DataTableSortMeta } from 'primevue';
import { FilterMatchMode, FilterOperator } from "@primevue/core/api"

const loading = ref(false);
const customers = ref<Customer[]>([]);
const possible_titles = ref<string[]>([]);

async function loadCustomers() {
    loading.value = true;
    customers.value = await fetchAllCustomers();
    possible_titles.value = [...new Set(customers.value.map(c => c.title))];
    loading.value = false;
}

const search_bar = useTemplateRef("search_bar");
// focus search with ctrl+k
onKeyStroke("k", (e) => {
    if (!e.ctrlKey)
    return
    // Ctrl+k at this point
    e.preventDefault()
    // @ts-expect-error
    search_bar.value.$el.focus()
})

onMounted(() => {
    loadCustomers()
})

const default_sorting: DataTableSortMeta[] = [
    {
        field: "customer_id",
        order: 1
    }
];

const filters = ref<DataTableFilterMeta>({});

function clearFilters() {
    filters.value = {
        global:        { value: null, matchMode: FilterMatchMode.CONTAINS },
        customer_id:   { value: null, matchMode: FilterMatchMode.GREATER_THAN },
        title:         { value: null, matchMode: FilterMatchMode.IN },
        first_name:    { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }]},
        last_name:     { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }]},
        date_of_birth: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_BEFORE }] },
        street:        { value: null, matchMode: FilterMatchMode.CONTAINS },
        postal_code:   { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        city:          { value: null, matchMode: FilterMatchMode.CONTAINS },
        email:         { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
}
clearFilters();

</script>

<template>
    <div class="flex flex-col gap-std w-full min-w-0">
        <Toolbar class="toolbar" :pt="{
            end: 'grow pl-10'
        }">
            <template #start>
                <Button :loading="loading" @click="loadCustomers" icon="pi pi-refresh" severity="secondary" text />
                <Button icon="pi pi-filter-slash" class="mr-2" severity="danger" text @click="clearFilters" />
                <Button icon="pi pi-plus" class="mr-2" severity="secondary" text disabled />
                <Button icon="pi pi-user-edit" class="mr-2" severity="secondary" text disabled />
                <Button icon="pi pi-trash" class="mr-2" severity="secondary" text disabled />
            </template>
    
            <template #end>
                <IconField class="w-full">
                    <InputIcon>
                        <i class="pi pi-search" />
                    </InputIcon>
                    <InputText 
                        class="w-full"
                        ref="search_bar" 
                        v-model="(filters['global'] as DataTableFilterMetaData).value" 
                        placeholder="Keyword Search (Ctrl+K)" 
                    />
                </IconField>
            </template>
        </Toolbar>
        
        <!-- 
        Need to make every node min-height: 0 up to the flex grow to prevent 
        them from expanding when the list grows 
        -->

        <Fieldset legend="List of customers" class="grow min-h-0 w-full min-w-0 overflow-hidden" :pt="{
            //legend: '!p-1',
            contentContainer: 'h-full min-h-0 w-full min-w-0',
            content: 'h-full min-h-0 w-full min-w-0'
        }">
            <div class="h-full min-h-0 w-full min-w-0">
                <DataTable 
                    :value="customers" 
                    striped-rows
                    sort-mode="multiple"
                    :multi-sort-meta="default_sorting"
                    removable-sort
                    v-model:filters="filters"
                    filter-display="menu"
                    :global-filter-fields="[
                        'customer_id',
                        'title',
                        'first_name',
                        'last_name',
                        'date_of_birth',
                        'street',
                        'postal_code',
                        'city',
                        'email',
                    ]"
                    selection-mode="multiple"
                    :loading="loading"
                    scrollable 
                    scroll
                    scrollHeight="flex" 
                    tableStyle="min-width: 50rem"
                >
                    <template #empty> No customers found. </template>
                    <template #loading> Loading customers data. Please wait. </template>
                    <Column field="customer_id" header="ID" data-type="numeric" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by ID" />
                        </template>
                    </Column>
                    <Column field="title" header="Title" :show-filter-match-modes="false">
                        <template #filter="{ filterModel, filterCallback }">
                            <MultiSelect 
                                v-model="filterModel.value" 
                                @change="filterCallback()" 
                                :options="possible_titles" 
                                placeholder="Any" 
                                style="min-width: 14rem" 
                                :maxSelectedLabels="1"
                            />
                        </template>
                    </Column>
                    <Column field="first_name" header="First" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by name" />
                        </template>
                    </Column>
                    <Column field="last_name" header="Last" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by name" />
                        </template>
                    </Column>
                    <Column field="date_of_birth" header="Date of birth" data-type="date" sortable >
                        <template #body="slotProps">
                            {{ (slotProps.data.date_of_birth as Date | null)?.toLocaleDateString() }}
                        </template>
                        <template #filter="{ filterModel }">
                            <DatePicker v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" />
                        </template>
                    </Column>
                    <Column field="street" header="Street" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by street" />
                        </template>
                    </Column>
                    <Column field="postal_code" header="ZIP" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by ZIP code" />
                        </template>
                    </Column>
                    <Column field="city" header="City" sortable >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by city" />
                        </template>
                    </Column>
                    <Column field="email" header="E-Mail" >
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by email" />
                        </template>
                    </Column>
                </DataTable>
            </div>
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