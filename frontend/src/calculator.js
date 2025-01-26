import "./assets/css/homestyle.css"
import { createApp } from 'vue'
import Calculator from './Calculator.vue'

createApp(Calculator).mount('#app')

export function getFlightData() {
    let departure = this.curloc;
    let destination = this.desloc;
    let response = fetch(`http://localhost:5000/process-flight-data?curloc=${departure}&desloc=${destination}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            curloc: departure,
            desloc: destination,
        }),
    });

}

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