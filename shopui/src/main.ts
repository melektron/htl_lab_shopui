import "./assets/main.css"

import { createApp } from "vue"
import router from "./router.ts";
import App from "./App.vue"

import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";
import { definePreset } from '@primevue/themes';

import InputText from "primevue/inputtext";
import InputIcon from "primevue/inputicon";
import IconField from "primevue/iconfield";
import Button from "primevue/button"
import Menubar from "primevue/menubar";
import Toolbar from "primevue/toolbar";
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import PanelMenu from "primevue/panelmenu";
import Dialog from "primevue/dialog";
import Card from "primevue/card";
import Fieldset from "primevue/fieldset";
import Message from "primevue/message";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import MultiSelect from "primevue/multiselect";
import DatePicker from "primevue/datepicker";


const app = createApp(App)

const MyThemePreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '{lime.50}',
            100: '{lime.100}',
            200: '{lime.200}',
            300: '{lime.300}',
            400: '{lime.400}',
            500: '{lime.500}',
            600: '{lime.600}',
            700: '{lime.700}',
            800: '{lime.800}',
            900: '{lime.900}',
            950: '{lime.950}'
        }
    }
});
app.use(PrimeVue, {
    theme: {
        preset: MyThemePreset
    }
});
app.use(ToastService);
app.use(router)

app.component("InputText", InputText);
app.component("Button", Button);
app.component("Menubar", Menubar);
app.component("Toolbar", Toolbar);
app.component("InputIcon", InputIcon);
app.component("IconField", IconField);
app.component("Toast", Toast);
app.component("PanelMenu", PanelMenu);
app.component("Dialog", Dialog);
app.component("Card", Card);
app.component("Fieldset", Fieldset);
app.component("Message", Message);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("MultiSelect", MultiSelect);
app.component("DatePicker", DatePicker);



app.mount("#app")
