<template>
    <InputGroup>
        <InputGroupAddon>
            <i class = "pi pi-lock"></i>
        </InputGroupAddon>
        <InputText ref = "textHolder" :type = "isVisible? 'text' : 'password' " v-model = val :placeholder = placeholder :label = fieldLabel @keydown = "getPass" />
        <Button icon :class = "isVisible? 'pi pi-eye' : 'pi pi-eye-slash'" @click = toggleVisibility />
    </InputGroup>
</template>

<script>
import InputGroup from "primevue/inputgroup"
import InputGroupAddon from "primevue/inputgroupaddon"
import InputText from "primevue/inputtext"
import Button from "primevue/button"

export default{
    name: "passField", 
    components: { InputGroup, InputGroupAddon, InputText, Button },
    props: {
        placeholder: String,
        fieldLabel: String,
    },
    data(){
        return{
            isVisible: false,
            val: "",
        }
    },
    methods: {
        toggleVisibility(){
            this.isVisible = !this.isVisible
        },

        getPass(){
            this.$emit("valChanged", this.$refs.textHolder.modelValue)
        }
    },
}
</script>