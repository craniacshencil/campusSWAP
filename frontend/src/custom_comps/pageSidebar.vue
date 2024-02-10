<template>
    <div class="card flex justify-content-center align-items-center">
        <Sidebar v-if="visible" v-model:visible="visible" header="sidebar">
            <Button @click = "visible = false">exit</Button>
            <p>lorem ipsum dolor sit amet, consectetur adipiscing elit
             ,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, 
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </Sidebar>
        <Button icon="pi pi-arrow-right" @click="visible = true" style = "margin-right: 184px" />
    </div>
</template>

<script>
import Sidebar from 'primevue/sidebar';
import Button from 'primevue/button';
export default{
    name: "pageSidebar",
    components: { Button, Sidebar },
    data(){
        return{
        visible: false,
        }
    },
}
</script>

