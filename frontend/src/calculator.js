import "./assets/css/homestyle.css"
import { createApp } from 'vue'
import Calculator from './Calculator.vue'

createApp(Calculator).mount('#app')


export async function getVehicleMakes() {
    return fetch(`http://localhost:5000/get-makes`)
}