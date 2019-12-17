<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <loading :active.sync="isLoading" :is-full-page="true"></loading>
      <SelectCIKs @updateCIKs="updateCIKs"/>
      <v-flex>
        <v-btn v-if="selectedCIKs.length > 0" @click='getTopics' color="green" dark>Generate Topics</v-btn>
      </v-flex>
      <TopicVisualization :chartData="chartData" />
    </v-layout>
  </v-container>
</template>

<script>
  import SelectCIKs from "./SelectCIKs";
  import TopicVisualization from "./TopicVisualization";
  import Loading from 'vue-loading-overlay';
  export default {
    name: 'Main',
    components: {
        SelectCIKs,
        TopicVisualization,
        Loading
    },
    data: () => ({
        selectedCIKs: [],
        chartData: [],
        isLoading: false
    }),
    methods: {
        updateCIKs (CIKs) {
          this.selectedCIKs = CIKs
        },
        getTopics () {
            this.isLoading = true
            let url = process.env.VUE_APP_API_URL + '/get_topics?'
            this.selectedCIKs.forEach((CIK) => {
                url += `CIKs=${CIK}&`
            })
            fetch(url)
                .then(response => response.json())
                .then((data) => {
                    this.chartData = data
                    this.isLoading = false
                })
        }
    }
  };
</script>
