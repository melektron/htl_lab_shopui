<script setup lang="ts">

import { ref } from "vue";
import Button from "primevue/button";
import { PanelMenu } from "primevue";
import type { MenuItem } from "primevue/menuitem";
import { useRoute } from "vue-router";

const items = ref<MenuItem[]>([
    {
        label: 'Home',
        icon: 'pi pi-home',
        route: "/"
    },
    {
        label: 'Customers',
        icon: 'pi pi-users',
        items: [
            {
                label: 'List View',
                icon: 'pi pi-list',
                route: "/customer/list"
            },
            {
                label: 'Analytics',
                icon: 'pi pi-chart-pie',
                route: "/customer/analytics"
            }
        ]
    },    
    {
        label: 'Files',
        icon: 'pi pi-file',
        items: [
            {
                label: 'Documents',
                icon: 'pi pi-file',
                items: [
                    {
                        label: 'Invoices',
                        icon: 'pi pi-file-pdf',
                        items: [
                            {
                                label: 'Pending',
                                icon: 'pi pi-stop'
                            },
                            {
                                label: 'Paid',
                                icon: 'pi pi-check-circle'
                            }
                        ]
                    },
                    {
                        label: 'Clients',
                        icon: 'pi pi-users'
                    }
                ]
            },
            {
                label: 'Images',
                icon: 'pi pi-image',
                items: [
                    {
                        label: 'Logos',
                        icon: 'pi pi-image'
                    }
                ]
            }
        ]
    },
    {
        label: 'Cloud',
        icon: 'pi pi-cloud',
        items: [
            {
                label: 'Upload',
                icon: 'pi pi-cloud-upload'
            },
            {
                label: 'Download',
                icon: 'pi pi-cloud-download'
            },
            {
                label: 'Sync',
                icon: 'pi pi-refresh'
            }
        ]
    },
    {
        label: 'Devices',
        icon: 'pi pi-desktop',
        items: [
            {
                label: 'Phone',
                icon: 'pi pi-mobile'
            },
            {
                label: 'Desktop',
                icon: 'pi pi-desktop'
            },
            {
                label: 'Tablet',
                icon: 'pi pi-tablet'
            }
        ]
    },
    {
        label: 'Help & About',
        icon: 'pi pi-question-circle',
        route: "/about"
    }
]);

const current_route = useRoute();

</script>


<template>
    <main class="w-full h-full gap-std p-std bg-surface-950">
        <div class="icon-wrapper flex justify-center items-center p-std rounded-2xl border-2 border-primary box-border gap-0.5">
            <span class="pi pi-shop !text-4xl pr-2"></span>
            <span class="leading-[100%] align-top text-4xl">
                ShopUI<sup>&reg</sup>
            </span>
        </div>
        <PanelMenu class="menu" :model="items" multiple>
            <template #item="{ item, active }">
                <RouterLink v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a 
                        v-ripple 
                        class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-3 py-2" 
                        :class="{
                            '!text-primary': current_route.fullPath === item.route
                        }"
                        :href="href" 
                        @click="navigate"
                    >
                        <span :class="item.icon" />
                        <span class="ml-2">{{ item.label }}</span>
                    </a>
                </RouterLink>
                <a v-else v-ripple class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-3 py-2" :href="item.url" :target="item.target">
                    <span :class="item.icon" />
                    <span class="ml-2">{{ item.label }}</span>
                    <span v-if="item.items" class="pi text-primary ml-auto" :class="{
                        'pi-angle-down': !active,
                        'pi-angle-up': active
                    }" />
                </a>
            </template>
        </PanelMenu>
        <RouterView class="content" />
    </main>
    <Toast />
</template>


<style scoped>

main {
    display: grid;
    grid:
        "icon content"
        "menu content";
    grid-template-columns: 15em 1fr;
    grid-template-rows: auto 1fr;
}

.icon-wrapper {
    grid-area: icon;
}

.menu {
    grid-area: menu;
}

.content {
    grid-area: content;
}
</style>
