import Vue from 'vue';

import Notification from '../components/Notification.vue';

const helpers = {
    methods: {
        createNotification: function (data) {
            /* create notification using the Notification component, functional abstraction */
            let propsData = {};
            if (data.time) {
                propsData.time = data.time;
            }
            if (data.context) {
                propsData.context = data.context;
            }
            if (data.message) {
                propsData.message = data.message;
            }
            const NotificationClass = Vue.extend(Notification);
            const instance = new NotificationClass({
                propsData: propsData,
            });
            instance.$mount();
            const parentNotification = document.getElementById('c-notification-vue');
            const firstNotification = parentNotification.firstChild;
            if (firstNotification) {
                parentNotification.insertBefore(instance.$el, firstNotification);
            } else {
                parentNotification.appendChild(instance.$el);
            }
        }
    }
};

export default helpers;