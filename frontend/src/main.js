import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueHighcharts from 'vue-highcharts'
import Highcharts from 'highcharts'
import loadWordcloud from 'highcharts/modules/wordcloud'

loadWordcloud(Highcharts);

Vue.use(VueHighcharts, { Highcharts })

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
