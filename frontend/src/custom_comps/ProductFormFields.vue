<template>
    <div class = "sell-form-fields-wrapper">
        <FloatLabel>
            <InputText id="Title of listing" v-model="title" class = "form-field" @input = "sendValues" required/>
            <label for="Title of listing">Title of listing</label>
        </FloatLabel>

        <FloatLabel>
            <InputText id="Category" v-model="category" class = "form-field" @input = "sendValues" required/>
            <label for="Category">Category</label>
        </FloatLabel>

        <FloatLabel>
            <InputText type = number id="Price" v-model="price" class = "form-field" @input= "sendValues" required/>
            <label for="Price">Price</label>
        </FloatLabel>

        <FloatLabel>
            <MultiSelect :showToggleAll="false" id="year" v-model="selectedYear" display = "chip" @change= "sendValues" :options = "engineeringYears" 
            class = "form-field" />
            <label for="year">Which year students need this item?</label>
        </FloatLabel>

        <FloatLabel>
            <MultiSelect :showToggleAll="false" id="Branch" v-model="selectedBranch" display = "chip" @change= "sendValues" :options = "engineeringBranch" 
            class = "form-field" />
            <label for="Branch">Which branch students would need this item?</label>
        </FloatLabel>

        <FloatLabel>
            <MultiSelect :showToggleAll="false" id="ItemType" v-model="selectedItemType" display = "chip" @change= "sendValues" :options = "itemType" 
            class = "form-field" />
            <label for="ItemType">Item type</label>
        </FloatLabel>

        <FloatLabel>
            <Dropdown id="Condition" v-model="selectedCondition" display = "chip"  @change= "sendValues"
            :options = "condition" class = "form-field" required/>
            <label for="Condition">Condition of Item</label>
        </FloatLabel>

        <FloatLabel>
            <Textarea class = "desc" v-model="productDesc" @input = "sendValues" required/>
            <label for="Product Description">Product Description</label>
        </FloatLabel>
    </div>
</template>
<script>
import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel'
import MultiSelect from 'primevue/multiselect';
import Dropdown from 'primevue/dropdown';
import Message from 'primevue/message';
export default{
    components: {Textarea, InputText, FloatLabel, MultiSelect, Dropdown, Message},
    name: ['ProductFormFields'],
    data(){
        return {
            engineeringYears: ["F.E", "S.E", "T.E", "B.E"],
            engineeringBranch: ["CS", "AIML", "DS", "Civil", "Mech", "EXTC", "IT"],
            itemType: ["Textbooks", "Stationery", "Tools", "Gadgets", "Electrical Components" ],
            condition: ["Brand New", "Used-Good Condition", "Used-Fair Condition", "Needs Repair" ],
            title: "",
            category: "",
            price: "",
            productDesc: "",
            selectedYear: [],
            selectedBranch: [],
            selectedItemType: [],
            selectedCondition: [],
        }
    },
    methods:{
        sendValues(){
            const fieldVals = {
                "title": this.title,
                "category": this.category,
                "price": this.price,
                "productDesc": this.productDesc,
                "selectedYear": this.selectedYear,
                "selectedBranch": this.selectedBranch,
                "selectedItemType": this.selectedItemType,
                "selectedCondition": this.selectedCondition,
            }
            this.$emit("receiveForm", fieldVals)
        },
    }
}
</script>

<style>
label{
    text-transform: uppercase;
    letter-spacing: 0.1rem;
}

.sell-form-fields-wrapper{
    display: flex;
    gap: 1.75rem;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.uploader-label{
    color: #AAA;
}
.form-field{
    width: 50vw;
    line-height: 2rem;
}

.image-uploader{
    margin-top: 1rem;
    width: 50vw;
    background: #09090b;
}
.desc{
    align-self: flex-start;
    background-color: #09090b;
    font-size: 16px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 10rem;
    min-width: 50vw;
}

.desc:focus{
    border: 1px solid teal;
    outline: 1px solid teal;
}
</style>