import {defineStore} from "pinia";

export const useMoneyStore = defineStore('moneyStore', {
    state() {
        return {
            money: [],
        }
    },
    actions: {
        setAlumnus(data) {
            this.money = data;
        }
    }
})
