import "./assets/css/homestyle.css"
import { createApp } from 'vue'
import Calculator from './Calculator.vue'

createApp(Calculator).mount('#app')

export function getFlightData() {
    let departure = this.curloc;
    let destination = this.desloc;
    return fetch(`http://localhost:5000/process-flight-data?curloc=${departure}&desloc=${destination}`, {method: "POST"})
}

export async function getVehicleMakes() {
    return fetch(`http://localhost:5000/get-makes`)
}