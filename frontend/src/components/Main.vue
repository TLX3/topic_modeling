<template>
  <v-container>
    <v-layout
      wrap
    >
      <loading :active.sync="isLoading" :is-full-page="true"></loading>
      <v-flex style="display: flex; justify-content: space-evenly;">
        <SelectCIKs @updateCIKs="updateCIKs" @updateNumTopics="updateNumTopics" @updateNgramNum="updateNgramNum" />
        <v-btn style="margin-top: 70px;" v-if="selectedCIKs.length > 0" @click='getTopics' color="green" dark>Generate Topics</v-btn>
      </v-flex>
      <TopicVisualization :chartData="chartData" :analyticsData="analyticsData"/>
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
        num_topics: 5,
        ngram_num: 3,
        chartData: [],
        analyticsData: [],
        isLoading: false
    }),
    methods: {
        updateCIKs (CIKs) {
          this.selectedCIKs = CIKs
        },
        updateNumTopics (num_topics) {
          this.num_topics = num_topics
        },
        updateNgramNum (ngram_num) {
            this.ngram_num = ngram_num
        },
        getTopics () {
            this.isLoading = true
            let url = process.env.VUE_APP_API_URL + '/get_topics?'
            this.selectedCIKs.forEach((CIK) => {
                url += `CIKs=${CIK}&`
            })
            url += `num_topics=${this.num_topics}&`
            url += `ngram_num=${this.ngram_num}`
            fetch(url)
                .then(response => response.json())
                .then((data) => {
                    /* eslint-disable no-console */
                    console.log(data)
                    /* eslint-enable no-console */
                    this.chartData = data[0]
                    this.analyticsData = data.slice(1)
                    this.isLoading = false
                })
        }
    }
  };
</script>
