import dataset.dataset as ds
import dataexploration.graphs.graphs as gr

df_ni= ds.read_dataset()
df=ds.read_imputed_onehot_dataset()
# ##gr.monthlyplot(df, target="NumberOfCustomers", save=True, show=False)
# ##gr.opendaybeforegeneralplot(df, 1000)
# gr.opendaybeforeonweekplot(df, 0)
# ##gr.competitorplot(df, "NumberOfCustomers", save=True, show=False)
# ##gr.frequencypershop(df, 0, target="NumberOfCustomers", shoptype=True, show=False, save=True)
# ##gr.scattertargets(df_ni, "StoreType", show=False, save=True)
# ##gr.availabilityplot(df)
# ##gr.frequencypershop(df, storeID=0, target="NumberOfCustomers", events=True, show=False, save=True)
# gr.barplot(df=df_ni, x="StoreType", hue="Region")
# gr.frequencystatplot(df)
# ##gr.monthlyplot(df, storetype=True, target="NumberOfCustomers", show=False, save=True)
# ##gr.monthlyplot(df, regions=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target="NumberOfCustomers", save=True, show=False)
gr.frequencypershop(df, target="NumberOfCustomers", storeID=-3)
# ##gr.promotionplot(df, show=False, save=True)
# gr.holidayplot(df)
# ##gr.meanstdscatterpershop(save=True)
# gr.monthlyplot(df, target="NumberOfCustomers", perstore=True)