import {defineStore} from "pinia";

export const useAllRolesStore = defineStore('allRolesStore', {
    state() {
        return {
            roles: [],
        }
    },
    actions: {
        setRoles(data) {
            this.roles = data;
        },
    }
})
