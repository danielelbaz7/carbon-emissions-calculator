import "./assets/css/homestyle.css"
import { createApp } from 'vue'
import Calculator from './Calculator.vue'

createApp(Calculator).mount('#app')


export async function getVehicleMakes() {
    return fetch(`http://localhost:5000/get-makes`)
}

export async function getVehicleModels(make) {
    return fetch(`http://localhost:5000/get-models?make=${make}`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
    })
}