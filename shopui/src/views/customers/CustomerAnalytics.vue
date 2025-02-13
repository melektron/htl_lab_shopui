<!--
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 21:45

Various charts about customers
-->

<script setup lang="ts">

</script>

<template>
    <div class="flex flex-col gap-std">
        <Toolbar class="toolbar">
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
                <SplitButton label="Save">
    
                </SplitButton>
                <span>hi </span>
            </template>
        </Toolbar>
        <Fieldset legend="Header" >
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </Fieldset>

        <Message severity="info" icon="pi pi-exclamation-triangle">
            <span >How may I help you?</span>
        </Message>


    </div>
</template>
