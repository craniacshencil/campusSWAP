export const userStore = {
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
    }
} 