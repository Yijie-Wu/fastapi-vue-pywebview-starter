import {defineStore} from "pinia";

export const useAllCarouselsStore = defineStore('allCarouselsStore', {
    state() {
        return {
            carousels: [],
        }
    },
    actions: {
        setCarousels(data) {
            this.carousels = data;
        },
        removeCarousels(id) {
            this.carousels = this.carousels.filter(carousel => carousel.id !== id);
        },
        updateCarousels(data) {
            this.carousels = this.carousels.map(carousel => {
                if (carousel.id === data.id) {
                    return data;
                }
                return carousel;
            });
        }
    }
})
