import './assets/style.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import 'primevue/resources/themes/aura-dark-cyan/theme.css'
import 'primeicons/primeicons.css'

import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Register from "./components/Register.vue"

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.use(router)
app.use(PrimeVue, { ripple: true})

app.mount('#app')
