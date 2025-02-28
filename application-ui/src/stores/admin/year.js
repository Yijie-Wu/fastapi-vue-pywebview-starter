import {defineStore} from "pinia";

export const useAllYearsStore = defineStore('allYearsStore', {
    state() {
        return {
            years: [],
        }
    },
    actions: {
        setYears(data) {
            this.years = data;
        },
        removeYears(id) {
            this.years = this.years.filter(year => year.id !== id);
        },
        updateYears(data) {
            this.years = this.years.map(year => {
                if (year.id === data.id) {
                    return data;
                }
                return year;
            });
        }
    }
})
