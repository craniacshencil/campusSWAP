// store/index.js
import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { userStore } from './modules/userModule'

const userState = createPersistedState({
    storage: window.sessionStorage,
    key: "user",
    paths: ["userStore.user"],
    getState: (key) => {
      let value = JSON.parse(sessionStorage.getItem(key))
      return value ? value.userStore : null;
    },
    setState: (key, value) => {
      value = JSON.stringify({ 'user' : value.userStore.user })
      return sessionStorage.setItem(key, value)
    }
})
const authState = createPersistedState({
    storage: window.sessionStorage,
    key: "isAuthenticated",
    paths: ["userStore.isAuthenticated"],
    getState: (key) => {
      const value = JSON.parse(sessionStorage.getItem(key))
      return value ? value.userStore : false;
    },
    setState: (key, value) => {
      value = JSON.stringify({ 'authState' : value.userStore.isAuthenticated })
      return sessionStorage.setItem(key, value)
    }
})
export const store = createStore({
  modules: {
    userStore,
  },
  plugins: [ userState, authState ]
})
