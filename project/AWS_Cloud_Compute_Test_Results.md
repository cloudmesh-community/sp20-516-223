# AWS Cloud Compute Test Results

## Benchmark

| Attribute  | Value  |
|---|---|
| cpu_count        | 4                                                                                                 |
| mem.active       | 5.9 GiB                                                                                           |
| mem.available    | 7.6 GiB                                                                                           |
| mem.free         | 1.2 GiB                                                                                           |
| mem.inactive     | 5.4 GiB                                                                                           |
| mem.percent      | 52.3 %                                                                                            |
| mem.total        | 16.0 GiB                                                                                          |
| mem.used         | 8.1 GiB                                                                                           |
| mem.wired        | 2.2 GiB                                                                                           |
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
| user             | rahul                                                                                             |                                                                                          |
|   |   |

## Results

### 05/02/20 - (SSH Failed) 

|Timer|Status|Time|Start|Cloud|
|---|---|---|---|---|
|test_00_sys/test_cms_help|ok|2.069|2020-05-02 06:49:00|aws|
| | | | | |
|test_02_key/test_clear_local_database|ok|0.043|2020-05-02 06:49:14|aws|
|test_02_key/test_clear_cloud_database|ok|0.019|2020-05-02 06:49:17|aws|
|test_02_key/test_upload_key_to_database|ok|0.057|2020-05-02 06:49:14|aws|
|test_02_key/test_upload_key_to_cloud|ok|0.136|2020-05-02 06:49:14|aws|
|test_02_key/test_list_key_from_cloud|ok|0.108|2020-05-02 06:49:14|aws|
|test_02_key/test_delete_key_from_cloud|ok|0.118|2020-05-02 06:49:15|aws|
|test_02_key/test_key_delete|ok|0.083|2020-05-02 06:49:15|aws|
|test_02_key/test_cms_local|ok|2.676|2020-05-02 06:49:15|aws|
|test_02_key/test_cms_cloud|ok|3.865|2020-05-02 06:49:17|aws|
| | | | | |
|test_04_flavor/test_empty_database|ok|0.037|2020-05-02 06:49:23|aws|
|test_04_flavor/test_provider_flavor|ok|186.555|2020-05-02 06:49:23|aws|
|test_04_flavor/test_provider_flavor_update|ok|386.076|2020-05-02 06:52:30|aws|
|test_04_flavor/test_cms_flavor_refresh|ok|205.427|2020-05-02 06:58:56|aws|
|test_04_flavor/test_cms_flavor|ok|8.03|2020-05-02 07:02:22|aws|
| | | | | |
|test_05_image/test_empty_database|ok|0.034|2020-05-02 07:02:32|aws|
|test_05_image/test_provider_image|failed|None|2020-05-02 07:02:32|aws|
|test_05_image/test_provider_image_update|failed|None|2020-05-02 07:03:58|aws|
|test_05_image/test_cms_image_refresh|ok|92.326|2020-05-02 07:05:24|aws|
|test_05_image/test_cms_image|ok|2.33|2020-05-02 07:06:57|aws|
| | | | | |
|test_07_secgroup_provider/test_load|ok|0.061|2020-05-02 07:07:03|aws|
|test_07_secgroup_provider/test_list_variables|ok|0.001|2020-05-02 07:07:04|aws|
|test_07_secgroup_provider/test_list_secgroups|ok|0.347|2020-05-02 07:07:04|aws|
|test_07_secgroup_provider/test_list_secgroups_rules|ok|0.092|2020-05-02 07:07:04|aws|
|test_07_secgroup_provider/test_secgroups_add|ok|0.186|2020-05-02 07:07:04|aws|
|test_07_secgroup_provider/test_upload_secgroup|ok|1.949|2020-05-02 07:07:05|aws|
|test_07_secgroup_provider/test_secgroups_delete|ok|0.209|2020-05-02 07:07:07|aws|
|test_07_secgroup_provider/test_secgroups_delete_again|ok|0.062|2020-05-02 07:07:07|aws|
| | | | | |
|test_08_vm_provider/test_provider_vm_create|ok|3.286|2020-05-02 07:22:58|aws|
|test_08_vm_provider/test_provider_vmprovider_vm_list|ok|0.367|2020-05-02 07:23:01|aws|
|test_08_vm_provider/test_provider_vm_wait|ok|0.06|2020-05-02 07:23:02|aws|
|test_08_vm_provider/test_provider_vm_ssh|failed|None|2020-05-02 07:23:02|aws|
|test_08_vm_provider/test_provider_vm_info|ok|0.24|2020-05-02 07:24:17|aws|
|test_08_vm_provider/test_vm_status|ok|0.117|2020-05-02 07:24:17|aws|
|test_08_vm_provider/test_provider_vm_stop|ok|30.961|2020-05-02 07:24:18|aws|
|test_08_vm_provider/test_provider_vm_start|ok|30.927|2020-05-02 07:24:54|aws|
|test_08_vm_provider/test_provider_vm_terminate|ok|30.713|2020-05-02 07:25:30|aws|
| | | | | |
|test_09_cm_names_find/test_cm_find_collection|ok|0.037|2020-05-02 07:26:07|aws|
|test_09_cm_names_find/test_cm_find_loop|ok|0.577|2020-05-02 07:26:07|aws|
|test_09_cm_names_find/test_cm_image_name_cloud|ok|0.021|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_image_name_collection|ok|0.024|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_names_regexp|ok|0.041|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_vms|ok|0.018|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_ubuntu_in_images|ok|0.018|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_cloud_name_attributes|ok|0.022|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_vm_collections|ok|0.022|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_vm_collections_vm|ok|0.02|2020-05-02 07:26:08|aws|
|test_09_cm_names_find/test_cm_find_vm_collection_form_parameter|ok|0.02|2020-05-02 07:26:08|aws|