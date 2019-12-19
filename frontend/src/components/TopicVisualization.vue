<template>
      <v-flex
        xs12
        mt-5
      >
          <v-card v-if="chartData.length > 0">
            <v-toolbar
                    color="#273a56"
                    dark
            >
              <v-toolbar-title v-if="showAnalytics">Analytics for Topics</v-toolbar-title>
              <div v-else>
              <v-toolbar-title v-if="currentView">Word Cloud for Topic #{{selectedTopic}}</v-toolbar-title>
              <v-toolbar-title v-else>Topic #{{selectedTopic}} Word Distribution</v-toolbar-title>
              </div>
              <v-spacer></v-spacer>
              <v-select
                      style="margin-top: 30px; max-width: 200px;"
                      color="#273a56"
                      solo
                      light
                  v-if="!showAnalytics && chartData.length > 0"
                  v-model="selectedTopic"
                  :items="topicNumbers"
                  label="Topic Number Ex: 1"
                  @change="refreshChartTopic"
              />
              <v-select
                      style="margin-top: 30px;"
                      color="#273a56"
                      solo
                      light
                  v-if="showAnalytics"
                  v-model="analyticsType"
                  :items="analyticsTypes"
                  label="Ex: Most representative Topic"
              />
              <v-btn
                      v-if="!showAnalytics"
                icon
                @click="currentView = !currentView"
              >
                <v-icon>{{ currentView ? 'mdi-table' : 'mdi-chart-bubble' }}</v-icon>
              </v-btn>
            </v-toolbar>
            <TopicAnalytics v-if='showAnalytics' :analyticsData="analyticsData" :analyticsType="analyticsType"/>
            <div v-else>
              <highcharts style="padding-top: 10px;" v-if='currentView' :options="chartOptions"></highcharts>
                <v-data-table
                        v-else
                :headers="headers"
                :items="chartData[selectedTopic - 1]"
                hide-default-footer
                class="elevation-1"
              ></v-data-table>
            </div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-tabs
                v-model="showAnalytics"
                color="#273a56"
                right
              >
                <v-tab>
                  SHOW DISTRIBUTION
                </v-tab>
                <v-tab>
                  SHOW ANALYTICS
                </v-tab>
              </v-tabs>
            </v-card-actions>
          </v-card>
      </v-flex>
</template>

<script>
  import TopicAnalytics from './TopicAnalytics'
    export default {
        name: 'SelectCIKs',
        components: {
            TopicAnalytics
        },
        props: ['chartData', 'analyticsData'],
        data: () => ({
            currentView: true,
            showAnalytics: 0,
            analyticsType: "Most representative document for topic",
            analyticsTypes: ["Dominant topic in each document", "Most representative document for topic"],
            headers: [
              { text: 'Term', value: 'term' },
              { text: 'Score', value: 'weight' }
            ],
            selectedTopic: 1,
            topicNumbers: [],
            chartOptions: {
                accessibility: {
                    screenReaderSection: {
                        beforeChartFormat: '<h5>{chartTitle}</h5>' +
                            '<div>{chartSubtitle}</div>' +
                            '<div>{chartLongdesc}</div>' +
                            '<div>{viewTableButton}</div>'
                    }
                },
                series: [{
                    type: 'wordcloud',
                    data:  [],
                    name: 'Score'
                }],
                title: {
                    text: 'LDA generated words'
                },
                credits: {
                  enabled: false
                }
            }
        }),
        methods: {
            refreshChartTopic () {
                let seriesData = []
                this.chartData[this.selectedTopic - 1].forEach((datum) => {
                    seriesData.push({
                        name: datum.term,
                        weight: datum.weight
                    })
                })
                let optionsCopy = JSON.parse(JSON.stringify(this.chartOptions))
                optionsCopy.series[0].data = seriesData
                this.chartOptions = optionsCopy
                /* eslint-disable no-console */
                console.log(this.chartOptions)
                /* eslint-enable no-console */
            }
        },
        watch: {
            chartData: function () {
                this.topicNumbers = []
                this.chartData.forEach((topic, i) => {
                    this.topicNumbers.push(i + 1)
                })
                this.refreshChartTopic()
            }
        }
    };
</script>
