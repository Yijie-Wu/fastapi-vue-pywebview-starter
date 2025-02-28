import {defineStore} from "pinia";

export const useCarouselsStore = defineStore('carouselsStore', {
    state() {
        return {
            carousels: [],
        }
    },
    actions: {
        setCarousels(data) {
            this.carousels = data;
        }
    }
})
