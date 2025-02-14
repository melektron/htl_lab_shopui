<!--
ELEKTRON © 2025 - now
Written by melektron
www.elektron.work
13.02.25, 17:37

About dialog that can be shown using
-->

<script setup lang="ts">
import { ref } from 'vue';


const visible = ref(false);

</script>

<template>
    <div class="flex flex-col justify-center items-center text-center text-lg">
        <div class="pb-6 px-16 border-b-8">
            <span class="pi pi-shop !text-9xl pr-2"></span>
            <span class="leading-[100%] align-top text-9xl">
                ShopUI<sup>&reg</sup>
            </span>
        </div>
        <p class="pt-6">
            The one and only solution to manage all your business needs.<br>
            From viewing to screwing your customers, we've got you covered!
        </p>
        <p class="pt-6 text-2xl">
            Start your Business today with ShopUI<sup>&reg</sup>
        </p>

        <p class="text-2xl flex gap-std">
            <Button label="Getting started" />
            <Button label="Credits" @click="visible = true"/>
        </p>
        
        <Dialog v-model:visible="visible" modal header="Credits">
            Developed by melektron & MrFlunter<br>
            &copy ELEKTRON 2025 - now<br>
            <span class="pi pi-github"/>
            <a 
                class="underline" 
                target="_blank" 
                rel="noopener noreferrer" 
                href="https://github.com/melektron/htl_lab_shopui"
            >
                melektron/htl_lab_shopui
            </a>
        </Dialog>
    </div>
</template>
