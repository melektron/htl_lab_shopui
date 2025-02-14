<!--
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 21:45

Various charts about customers
-->

<script setup lang="ts">

import { ref, onMounted } from "vue";

import { fetchAllCustomers } from '@/api';
import type { Customer } from '@/api';

const loading = ref(false);

const pie_chart_data = ref();
const pie_chart_options = ref();
const line_chart_data = ref();
const line_chart_options = ref();
const unknown_age_count = ref(0);
const total_customer_count = ref(0);


async function fetchAndCompute() {
    loading.value = true;
    
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color');
    const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color');
    
    const customers = await fetchAllCustomers();
    total_customer_count.value = customers.length
    
    const title_distribution = customers.reduce<{[key: string]: number}>((acc, c, _) => {
        if (c.title in acc) {
            acc[c.title] += 1
        } else {
            acc[c.title] = 1
        }
        return acc
    }, {});
    const titles = Object.keys(title_distribution)
    const title_counts = Object.values(title_distribution)

    const age_granularity = 10  // how many years to consolidate
    const current_year = new Date(Date.now()).getFullYear()
    const age_distribution = customers.reduce<{
        unknown: number,
        below: {[key: number]: number}
    }> ((acc, c, _) => {
        const birth_year = c.date_of_birth?.getFullYear()
        if (birth_year == null)
            acc.unknown++
        else {
            // calculate in which consolidation range we lie
            const age = current_year - birth_year
            const range = Math.ceil(age / age_granularity) * age_granularity
            // at thsi point, range will be a multiple of age_granularity
            if (range in acc.below) {
                acc.below[range] += 1
            } else {
                acc.below[range] = 1
            }
        }
        return acc
    }, {
        unknown: 0,
        below: {}
    });
    const populated_age_ranges = Object.keys(age_distribution.below).map(k => +k)
    const max_range = Math.max(...populated_age_ranges);
    const all_age_ranges: string[] = [] 
    const all_age_range_counts: number[] = []
    for (let i = age_granularity; i <= max_range; i += age_granularity) {
        all_age_ranges.push(`<${i}`)
        if (i in age_distribution.below) {
            all_age_range_counts.push(age_distribution.below[i])
        } else {
            all_age_range_counts.push(0)
        }
    }
    unknown_age_count.value = age_distribution.unknown
    
    pie_chart_data.value =  {
        labels: titles,
        datasets: [
            {
                data: title_counts,
                backgroundColor: [documentStyle.getPropertyValue('--p-lime-500'), documentStyle.getPropertyValue('--p-orange-500'), documentStyle.getPropertyValue('--p-gray-500')],
                hoverBackgroundColor: [documentStyle.getPropertyValue('--p-lime-400'), documentStyle.getPropertyValue('--p-orange-400'), documentStyle.getPropertyValue('--p-gray-400')]
            }
        ]
    };
    pie_chart_options.value = {
        plugins: {
            legend: {
                labels: {
                    usePointStyle: true,
                    color: textColor
                }
            }
        }
    };
    
    line_chart_data.value = {
        labels: all_age_ranges,
        datasets: [
            {
                label: 'Number of Customers',
                data: all_age_range_counts,
                fill: false,
                borderColor: documentStyle.getPropertyValue('--p-lime-500'),
                tension: 0.4
            },
            //{
            //    label: 'Second Dataset',
            //    data: [28, 48, 40, 19, 86, 27, 90],
            //    fill: false,
            //    borderColor: documentStyle.getPropertyValue('--p-gray-500'),
            //    tension: 0.4
            //}
        ]
    };
    line_chart_options.value = {
        maintainAspectRatio: false,
        aspectRatio: 0.6,
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            },
            y: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            }
        }
    };

    loading.value = false;
}
onMounted(fetchAndCompute)

</script>

<template>
    <div class="flex flex-col gap-std">
        <Toolbar class="toolbar" :pt="{
            end: 'grow pl-10'
        }">
            <template #start>
                <Button :loading="loading" @click="fetchAndCompute" icon="pi pi-refresh" severity="secondary" text />
            </template>
    
        </Toolbar>
        <div class="flex justify-center gap-10 w-full">
            <div class="flex flex-col gap-10">
                <Chart type="pie" :data="pie_chart_data" :options="pie_chart_options" class="w-full md:w-[30rem]" />
                <Card>
                    <template #title>Title distribution</template>
                    <template #content>
                        <p class="m-0">
                            This chart shows the distribution of titles among the customer base. Interrestingly, 
                            the majority of them seem to be female, while a significant portion apparantly didn't
                            no what a title was. Surprisingly, there are no academics in the customer base. 
                        </p>
                    </template>
                </Card>
            </div>
            <div class="grow flex flex-col gap-10">
                <Chart type="line" :data="line_chart_data" :options="line_chart_options" class="h-[30rem]" />
                <Card>
                    <template #title>Customer age distribution</template>
                    <template #content>
                        <p class="m-0">
                            This chart shows the distribution of age among the customer base. The X-Axis shows 
                            the age of customers, the Y-Axis the amount of customers at that age. As expected, most custsomers
                            are in their forties or fifties. Surprisingly though, there are almost no customers younger than 40 years.
                            Instead, there seem to be a lot of customers in their mighty hundreds. Our products must be very
                            healthy. It is important to mention that {{ unknown_age_count }} out of {{ total_customer_count }} customers
                            have provided their age, so this analysis might not be entirely conclusive. It might also suggest that 
                            younger people think more about their privacy before givin away information such as birthdays.
                        </p>
                    </template>
                </Card>
            </div>
        </div>




    </div>
</template>
