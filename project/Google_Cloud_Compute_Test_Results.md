# Google Cloud Compute Test Results

## Benchmark

| Attribute  | Value  |
|---|---|
| cpu_count        | 4                                                                                                 |
| mem.active       | 6.8 GiB                                                                                           |
| mem.available    | 7.2 GiB                                                                                           |
| mem.free         | 403.4 MiB                                                                                         |
| mem.inactive     | 5.8 GiB                                                                                           |
| mem.percent      | 54.9 %                                                                                            |
| mem.total        | 16.0 GiB                                                                                          |
| mem.used         | 8.8 GiB                                                                                           |
| mem.wired        | 2.0 GiB                                                                                           |
| platform.version | 10.14.6                                                                                           |
| python           | 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53)                                                  |
|                  | [Clang 6.0 (clang-600.0.57)]                                                                      |
| python.pip       | 20.0.2                                                                                            |
| python.version   | 3.8.1                                                                                             |
| sys.platform     | darwin                                                                                            |
| uname.machine    | x86_64                                                                                            |
| uname.node       | rjdharmc-mac                                                                                      |
| uname.processor  | i386                                                                                              |
| uname.release    | 18.7.0                                                                                            |
| uname.system     | Darwin                                                                                            |
| uname.version    | Darwin Kernel Version 18.7.0: Mon Feb 10 21:08:45 PST 2020; root:xnu-4903.278.28~1/RELEASE_X86_64 |
| user             | rahul                                                                                             |
|   |   |

## Results

### 04/26/20 - Fixed SSH Failure. 

|Timer|Status|Time|Start|Cloud|
|---|---|---|---|---|
|test_00_sys/test_cms_help|ok|1.476|2020-04-26 21:29:43|google|
| | | | | |
|test_02_key/test_clear_local_database|ok|0.047|2020-04-26 21:30:12|google|
|test_02_key/test_clear_cloud_database|ok|0.025|2020-04-26 21:30:51|google|
|test_02_key/test_upload_key_to_database|ok|0.061|2020-04-26 21:30:12|google|
|test_02_key/test_upload_key_to_cloud|ok|18.668|2020-04-26 21:30:13|google|
|test_02_key/test_list_key_from_cloud|ok|1.481|2020-04-26 21:30:32|google|
|test_02_key/test_delete_key_from_cloud|ok|15.084|2020-04-26 21:30:33|google|
|test_02_key/test_key_delete|ok|0.039|2020-04-26 21:30:48|google|
|test_02_key/test_cms_local|ok|2.461|2020-04-26 21:30:48|google|
|test_02_key/test_cms_cloud|ok|15.991|2020-04-26 21:30:51|google|
| | | | | |
|test_04_flavor/test_empty_database|ok|0.03|2020-04-26 21:31:08|google|
|test_04_flavor/test_provider_flavor|ok|1.367|2020-04-26 21:31:08|google|
|test_04_flavor/test_provider_flavor_update|ok|1.392|2020-04-26 21:31:09|google|
|test_04_flavor/test_cms_flavor_refresh|ok|2.324|2020-04-26 21:31:11|google|
|test_04_flavor/test_cms_flavor|ok|1.38|2020-04-26 21:31:13|google|
| | | | | |
|test_05_image/test_empty_database|ok|0.03|2020-04-26 21:31:16|google|
|test_05_image/test_provider_image|ok|5.664|2020-04-26 21:31:16|google|
|test_05_image/test_provider_image_update|ok|5.4|2020-04-26 21:31:22|google|
|test_05_image/test_cms_image_refresh|ok|6.614|2020-04-26 21:31:28|google|
|test_05_image/test_cms_image|ok|1.374|2020-04-26 21:31:34|google|
| | | | | |
|test_07_secgroup_provider/test_load|ok|0.043|2020-04-26 21:31:37|google|
|test_07_secgroup_provider/test_list_variables|ok|0.001|2020-04-26 21:31:37|google|
|test_07_secgroup_provider/test_list_secgroups|ok|1.256|2020-04-26 21:31:37|google|
|test_07_secgroup_provider/test_list_secgroups_rules|ok|1.22|2020-04-26 21:31:39|google|
|test_07_secgroup_provider/test_secgroups_add|ok|0.043|2020-04-26 21:31:40|google|
|test_07_secgroup_provider/test_upload_secgroup|ok|18.833|2020-04-26 21:31:41|google|
|test_07_secgroup_provider/test_secgroups_delete|ok|24.561|2020-04-26 21:32:01|google|
|test_07_secgroup_provider/test_secgroups_delete_again|ok|2.179|2020-04-26 21:32:27|google|
| | | | | |
|test_08_vm_provider/test_provider_vm_create|ok|17.684|2020-04-26 21:33:09|google|
|test_08_vm_provider/test_provider_vmprovider_vm_list|ok|1.242|2020-04-26 21:33:28|google|
|test_08_vm_provider/test_provider_vm_wait|ok|24.773|2020-04-26 21:33:29|google|
|test_08_vm_provider/test_provider_vm_ssh|ok|2.077|2020-04-26 21:33:57|google|
|test_08_vm_provider/test_provider_vm_info|ok|1.365|2020-04-26 21:33:59|google|
|test_08_vm_provider/test_vm_status|ok|1.233|2020-04-26 21:34:00|google|
|test_08_vm_provider/test_provider_vm_stop|ok|28.075|2020-04-26 21:34:02|google|
|test_08_vm_provider/test_provider_vm_start|ok|8.503|2020-04-26 21:34:36|google|
|test_08_vm_provider/test_provider_vm_terminate|ok|147.044|2020-04-26 21:34:51|google|
| | | | | |
|test_09_cm_names_find/test_cm_find_collection|ok|0.031|2020-04-26 21:37:24|google|
|test_09_cm_names_find/test_cm_find_loop|ok|0.067|2020-04-26 21:37:24|google|
|test_09_cm_names_find/test_cm_image_name_cloud|ok|0.022|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_image_name_collection|ok|0.022|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_names_regexp|ok|0.042|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_vms|ok|0.02|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_ubuntu_in_images|ok|0.02|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_cloud_name_attributes|ok|0.02|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_vm_collections|ok|0.019|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_vm_collections_vm|ok|0.019|2020-04-26 21:37:25|google|
|test_09_cm_names_find/test_cm_find_vm_collection_form_parameter|ok|0.018|2020-04-26 21:37:25|google|

### 04/25/20 

|Timer|Status|Time|Start|Tag|
|---|---|---|---|---|
|test_00_sys/|test_cms_help|ok|1.968|2020-04-25 23:30:32|google|
|   |   |   |   |   |
|test_02_key/|test_clear_local_database|ok|0.042|2020-04-25 23:30:45|google|
|test_02_key/|test_clear_cloud_database|ok|0.022|2020-04-25 23:31:16|google|
|test_02_key/|test_upload_key_to_database|ok|0.063|2020-04-25 23:30:45|google|
|test_02_key/|test_upload_key_to_cloud|ok|13.463|2020-04-25 23:30:45|google|
|test_02_key/|test_list_key_from_cloud|ok|1.471|2020-04-25 23:30:59|google|
|test_02_key/|test_delete_key_from_cloud|ok|13.473|2020-04-25 23:31:00|google|
|test_02_key/|test_key_delete|ok|0.044|2020-04-25 23:31:14|google|
|test_02_key/|test_cms_local|ok|2.573|2020-04-25 23:31:14|google|
|test_02_key/|test_cms_cloud|ok|20.694|2020-04-25 23:31:16|google|
|   |   |   |   |   |
|test_04_flavor/|test_empty_database|ok|0.028|2020-04-25 23:31:38|google|
|test_04_flavor/|test_provider_flavor|ok|1.31|2020-04-25 23:31:38|google|
|test_04_flavor/|test_provider_flavor_update|ok|1.49|2020-04-25 23:31:40|google|
|test_04_flavor/|test_cms_flavor_refresh|ok|2.797|2020-04-25 23:31:42|google|
|test_04_flavor/|test_cms_flavor|ok|1.337|2020-04-25 23:31:45|google|
|   |   |   |   |   |
|test_05_image/|test_empty_database|ok|0.037|2020-04-25 23:31:47|google|
|test_05_image/|test_provider_image|ok|5.271|2020-04-25 23:31:47|google|
|test_05_image/|test_provider_image_update|ok|4.681|2020-04-25 23:31:53|google|
|test_05_image/|test_cms_image_refresh|ok|6.065|2020-04-25 23:31:58|google|
|test_05_image/|test_cms_image|ok|1.344|2020-04-25 23:32:04|google|
|   |   |   |   |   |
|test_07_secgroup_provider/|test_load|ok|0.047|2020-04-25 23:32:06|google|
|test_07_secgroup_provider/|test_list_variables|ok|0.001|2020-04-25 23:32:07|google|
|test_07_secgroup_provider/|test_list_secgroups|ok|1.593|2020-04-25 23:32:07|google|
|test_07_secgroup_provider/|test_list_secgroups_rules|ok|1.423|2020-04-25 23:32:08|google|
|test_07_secgroup_provider/|test_secgroups_add|ok|0.04|2020-04-25 23:32:10|google|
|test_07_secgroup_provider/|test_upload_secgroup|ok|16.989|2020-04-25 23:32:11|google|
|test_07_secgroup_provider/|test_secgroups_delete|ok|16.373|2020-04-25 23:32:29|google|
|test_07_secgroup_provider/|test_secgroups_delete_again|ok|2.272|2020-04-25 23:32:47|google|
|   |   |   |   |   |
|test_08_vm_provider/|test_provider_vm_create|ok|18.565|2020-04-25 23:33:29|google|
|test_08_vm_provider/|test_provider_vmprovider_vm_list|ok|1.438|2020-04-25 23:33:49|google|
|test_08_vm_provider/|test_provider_vm_wait|ok|0.057|2020-04-25 23:33:50|google|
|test_08_vm_provider/|test_provider_vm_ssh|failed|None|2020-04-25 23:33:50|google|
|test_08_vm_provider/|test_provider_vm_info|ok|1.211|2020-04-25 23:33:52|google|
|test_08_vm_provider/|test_vm_status|ok|1.159|2020-04-25 23:33:53|google|
|test_08_vm_provider/|test_provider_vm_stop|ok|35.242|2020-04-25 23:33:54|google|
|test_08_vm_provider/|test_provider_vm_start|ok|10.038|2020-04-25 23:34:36|google|
|test_08_vm_provider/|test_provider_vm_terminate|ok|146.026|2020-04-25 23:34:52|google|
|   |   |   |   |   |
|test_09_cm_names_find/|test_cm_find_collection|ok|0.035|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_loop|ok|0.073|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_image_name_cloud|ok|0.02|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_image_name_collection|ok|0.022|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_names_regexp|ok|0.034|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_vms|ok|0.02|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_ubuntu_in_images|ok|0.019|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_cloud_name_attributes|ok|0.02|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_vm_collections|ok|0.018|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_vm_collections_vm|ok|0.02|2020-04-25 23:37:25|google|
|test_09_cm_names_find/|test_cm_find_vm_collection_form_parameter|ok|0.017|2020-04-25 23:37:25|google|
