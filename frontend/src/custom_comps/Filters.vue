<template>
    <div class="card flex justify-content-center align-items-center">
        <Sidebar class = "filters" v-model:visible="visible" position = "right">
            <div class = "filter-container">
                <Panel collapsed = true class="filter-field" header="YEAR" toggleable>
                    <div class="flex flex-column gap-3">
                        <div v-for="year of engineeringYears" :key="year" class="flex align-items-center">
                            <Checkbox v-model="selectedYear" :inputId = "year" name = "year" :value="year" />
                            <label :for="year">{{year}}</label>
                        </div>
                    </div>
                </Panel>

                <Panel collapsed = true class="filter-field" header="BRANCH" toggleable>
                    <div class="flex flex-column gap-3">
                        <div v-for="branch of engineeringBranch" :key="branch" class="flex align-items-center">
                            <Checkbox v-model="selectedBranch" :inputId = "branch" name = "branch" :value="branch" />
                            <label :for="branch">{{branch}}</label>
                        </div>
                    </div>
                </Panel>

                <Panel collapsed = true class="filter-field" header="TYPE" toggleable>
                    <div class="flex flex-column gap-3">
                        <div v-for="types of itemType" :key="types" class="flex align-items-center">
                            <Checkbox v-model="selectedItemType" :inputId = "types" name = "types" :value="types" />
                            <label :for="types">{{types}}</label>
                        </div>
                    </div>
                </Panel>

                <Panel collapsed = true class= 'filter-field' header='CONDITION' toggleable>
                    <div class="flex flex-column gap-3">
                        <div v-for="condition in conditions" :key="condition" class="flex align-items-center">
                            <RadioButton v-model="selectedCondition" :inputId="condition" name="condition" :value="condition" />
                            <label :for="condition" class="ml-2">{{condition}}</label>
                        </div>
                    </div>
                </Panel>

                <Panel collapsed = true class="filter-field" header="SORT BY" toggleable>
                    <div class="flex flex-column gap-3">
                        <div v-for="SortCondition in sorts" :key="SortCondition" class="flex align-items-center">
                            <RadioButton v-model="selectedVal" :inputId="SortCondition" name="SortCondition" :value="SortCondition" />
                            <label :for="SortCondition" class="ml-2">{{SortCondition}}</label>
                        </div>
                    </div>
                </Panel>

                <Button class = "first-btn filter-field filter-btn" severity = "contrast" raised label = "Apply Filters" @click = "applyFilters" />
                <Button class = "filter-field filter-btn" severity = "secondary" raised label = "Reset Filters" @click = "resetFilters" />
            </div>
        </Sidebar>
        <Button class = "main-btn" label = "FILTERS" @click="visible = true" icon="pi pi-filter" />
    </div>
</template>

<script>
import Sidebar from 'primevue/sidebar';
import Checkbox from 'primevue/checkbox';
import Button from 'primevue/button';
import MultiSelect from 'primevue/multiselect';
import Dropdown from 'primevue/dropdown';
import Panel from 'primevue/panel';
import RadioButton from 'primevue/radiobutton';
export default{
    name: "pageSidebar",
    components: { RadioButton, Checkbox, Panel, MultiSelect, Dropdown, Button, Sidebar },
    data(){
        return{
        visible: false,
        engineeringYears: ["F.E", "S.E", "T.E", "B.E"],
        engineeringBranch: ["CS", "AIML", "DS", "Civil", "Mech", "EXTC", "IT"],
        itemType: ["Textbooks", "Stationery", "Tools", "Gadgets", "Electrical Components"],
        conditions: ["Brand New", "Used-Good Condition", "Used-Fair Condition", "Needs Repair"],
        sorts: ["Price: Low to High", "Price: High to Low", "Newly Listed", "Seller rating" ],
        selectedYear: [],
        selectedBranch: [],
        selectedItemType: [],
        selectedCondition: "",
        selectedVal: "",
        }
    },
    methods: {
        resetFilters(){
            this.selectedYear = []
            this.selectedBranch = []
            this.selectedItemType = [] 
            this.selectedCondition = ""
            this.selectedVal = ""
            console.log(this.selectedYear)
        },

        applyFilters(){
            const filterValues = [
                { 'year' : this.selectedYear },
                { 'branch': this.selectedBranch },
                { 'itemType': this.selectedItemType },
                { 'condition' : this.selectedCondition },
                { 'sort': this.selectedVal },
            ]
            this.$emit('getFiltersVal', filterValues)
        }
    },
}
</script>

<style> 
/* when i scope these styles the primevue api theming does not apply  */
.filters{
    width: 50%;
}

.filter-container{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.filter-field{
    width: 70%;
    font-weight: 300;
}

.filters label{
    margin-left: 0.5rem;
}

.filter label:hover{
    text-decoration: underline;
}

.filters .p-panel{
    border: none;
}

.filters .p-panel-header{
    padding: 0.5rem;
    letter-spacing: -.1rem;
}

.filters .p-panel-title{
    font-weight: 300;
}

.filters .p-sidebar-header{
    margin-left: auto;
}

.filter-btn{
    text-transform: uppercase;
    letter-spacing: -.1rem;
    border-radius: 0;
    margin: 0.5rem;
}

.first-btn{
    margin-top: 3rem;
}

.main-btn{
    border-radius: 0;
    font-weight: 700;
}
</style>