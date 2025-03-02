import {defineStore} from "pinia";

export const useSettingStore = defineStore('settingStore', {
    state() {
        return {
            setting: {},
        }
    },
    actions: {
        setItem(data) {
            this.setting = data;
        },
        getItem() {
            return this.setting;
        },
        updateItem(data) {
            this.setting = data;
        }
    }
})
