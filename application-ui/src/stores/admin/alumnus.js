import {defineStore} from "pinia";

export const useAllAlumnusStore = defineStore('allAlumnusStore', {
    state() {
        return {
            alumnuss: [],
        }
    },
    actions: {
        setAlumnus(data) {
            this.alumnuss = data;
        },
        addAlumnus(data) {
            this.alumnuss.push(data);
        },
        updateAlumnus(data) {
            this.alumnuss = this.alumnuss.map(alumnus => {
                if (alumnus.id === data.id) {
                    return data;
                }
                return alumnus;
            });
        },
        removeAlumnus(id) {
            this.alumnuss = this.alumnuss.filter(alumnus => alumnus.id !== id);
        },
    }
})
