<template>
      <v-flex
        xs12
        mt-5
      >
        <h2 v-if="chartData.length > 0" class="headline font-weight-bold">Word Cloud for Topic #{{selectedTopic + 1}}</h2>
        <h4 v-if="chartData.length > 0" class="headline my-3">Select Topic Number</h4>
        <v-select
                v-if="chartData.length > 0"
                v-model="selectedTopic"
                :items="topicNumbers"
                label="Ex: 1"
                solo
                @change="refreshChartTopic"
        />
        <highcharts v-if="chartData.length > 0" :options="chartOptions"></highcharts>
      </v-flex>
</template>

<script>
    export default {
        name: 'SelectCIKs',
        props: ['chartData'],
        data: () => ({
            selectedTopic: 0,
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
                    name: 'Weight'
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
                this.chartData[this.selectedTopic].forEach((datum) => {
                    seriesData.push({
                        name: datum.term,
                        weight: datum.weight * 100
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
                    this.topicNumbers.push(i)
                })

                this.refreshChartTopic()
            }
        }
    };
</script>
