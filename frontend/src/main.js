import './assets/style.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css'
import 'primevue/resources/themes/aura-dark-cyan/theme.css'
import 'primeicons/primeicons.css'

import Home from "./pages/Home.vue"
import Login from "./pages/Login.vue"
import Register from "./pages/Register.vue"
import Test from "./pages/test.vue"
import Buy from "./pages/Buy.vue"
import Wishlist from "./pages/Wishlist.vue"
import Sell from "./pages/Sell.vue"
import Settings from "./pages/Settings.vue"

const routes = [
    { path: '/', component: Home, name: "Home" },
    { path: '/login', component: Login, name: "Login"},
    { path: '/register', component: Register, name: "Register"},
    { path: '/buy', component: Buy, name: "Buy" },
    { path: '/wishlist', component: Wishlist, name: "Wishlist" },
    { path: '/sell', component: Sell, name: "Sell" },
    { path: '/settings', component: Settings, name: "Settings" },

]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.use(router)
app.use(PrimeVue, { ripple: true})

app.mount('#app')
