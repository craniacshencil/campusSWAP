//vuex state management
import { createStore } from 'vuex'
export default createStore({
    state(){
        return{
            isAuthenticated: false,
            user: null,
        }
    },

    mutations: {
        toggleIsAuthenticated(state){
            state.isAuthenticated = !state.isAuthenticated 
        },
        
        assignUser(state, newUser){
            state.user = newUser
        },
    },

    // actions: {
    //     login({ commit }){
    //         axios.post('http://localhost:8000/apis/login', {
    //             moodleID: this.moodleID,
    //             passText: this.passText,
    //         }, { withCredentials: true})
    //         .then(response => {
    //             commit('setLoginError', response.data.login_error)
    //             commit('toggleIsAuthenticated')
    //             commit('assignUser', user)
    //             if(this.loginError == "No Error"){
    //                 setTimeout(() => {this.$router.push('/')}, 750)
    //             }
    //         })
    //         .catch(error => {
    //             console.log(error);
    //         });
    //     },

    //     logout({ commit }){
    //         axios.post('http://localhost:8000/apis/logout', {
    //         })
    //         .then(response => {
    //             commit('toggleIsAuthenticated')
    //             commit('assignUser', null)
    //             setTimeout(() => {this.$router.push('login')}, 800)
    //         })
    //         .catch(error => {
    //             console.log(error);
    //         });
    //     }
    // }
})