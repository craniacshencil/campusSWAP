<template>
    <nav class = "main-wrapper flex justify-content-end">
        <router-link to = "/" class = "nav-part home">Home</router-link>
        <router-link to = "/login" class = "nav-part login">Login</router-link>
        <router-link to = "/register" class = "nav-part register">Register</router-link>
    </nav>
</template>

<script>
export default{
    name: ['PrimaryNav'],
}
</script>

<style scoped>
.main-wrapper{
    margin-top: .5rem;
    margin-right: 2rem;
    gap: 1rem;
    width: 100%;
}
.nav-part{
    padding: 0.5rem 1rem;
    font-size: 1.2rem;
    text-decoration: none;
    color: white; 
}
.nav-part:hover{
    border-bottom: 0.1rem solid white;
}

.router-link-active{
    border-bottom: 0.1rem solid white;
}
</style>
