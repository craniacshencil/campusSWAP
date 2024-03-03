import './assets/style.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import store from './store'
import { createRouter, createWebHistory } from 'vue-router'
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css'
import 'primevue/resources/themes/aura-dark-cyan/theme.css'
import 'primeicons/primeicons.css'
import axios from 'axios'

//router code
import Home from "./pages/Home.vue"
import Login from "./pages/Login.vue"
import Register from "./pages/Register.vue"
import Buy from "./pages/Buy.vue"
import Wishlist from "./pages/Wishlist.vue"
import Sell from "./pages/Sell.vue"
import Settings from "./pages/Settings.vue"
import { userStore } from './store/modules/userModule'

const routes = [
    { path: '/', component: Home, name: "Home"},
    { path: '/login', component: Login, name: "Login"},
    { path: '/register', component: Register, name: "Register"},
    { path: '/buy', component: Buy, name: "Buy", meta: {
        authenticationRequired: true
    }},
    { path: '/wishlist', component: Wishlist, name: "Wishlist", meta: {
        authenticationRequired: true
    } },
    { path: '/sell', component: Sell, name: "Sell", meta: {
        authenticationRequired: true
    }},
    { path: '/settings', component: Settings, name: "Settings", meta: {
        authenticationRequired: true
    }},

]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to, from) => {
    if(to.meta.authenticationRequired){
        const isAuthenticatedString= sessionStorage.getItem('isAuthenticated')
        const isAuthenticatedJson = JSON.parse(isAuthenticatedString)
        if(!(isAuthenticatedJson.userStore.isAuthenticated)){
            return { name: "Login" }
        }
    }
})

const app = createApp(App)
app.use(ToastService);
app.use(ConfirmationService);
app.use(router)
app.use(store)
app.use(PrimeVue, { ripple: true})

app.mount('#app')
