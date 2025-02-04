<script setup lang="ts">

import { ref } from "vue";
import Button from "primevue/button";

</script>


<template>
    <main>
        <div class="bar-wrapper">
            <Toolbar>
                <template #start>
                    <Button icon="pi pi-refresh " severity="secondary" text />
                    <Button icon="pi pi-plus" class="mr-2" severity="secondary" text />
                    <Button icon="pi pi-print" class="mr-2" severity="secondary" text />
                    <Button icon="pi pi-upload" severity="secondary" text />
                </template>

                <template #center>
                    <IconField>
                        <InputIcon>
                            <i class="pi pi-search" />
                        </InputIcon>
                        <InputText placeholder="Search" />
                    </IconField>
                </template>

                <template #end> 
                    <SplitButton label="Save" :model="items">

                    </SplitButton>
                    <span>hi </span>
                </template>
            </Toolbar>
        </div>
        
    </main>
    <Toast />
</template>


<style scoped>
main {
    width: 100%;
    height: 100%;
    box-sizing: border-box;

    grid:
        "bar"
        "table";
    grid-template-columns: 1fr;
    grid-template-rows: 3em 1fr;
}

.menu-wrapper

.bar-wrapper {
    grid-area: bar;

}
</style>
