#include "sm_mac.h"
#include "../../../test/rnd/fill_rnd_data_mac.h"
#include <assert.h>

void init_mac_sm(void)
{
  // No allocation needed
}

void free_mac_sm(void)
{
  // No allocation needed
}



bool read_mac_sm(void* data)
{
  assert(data != NULL);
//  assert(data->type == MAC_STATS_V0);

  mac_ind_data_t* mac = (mac_ind_data_t*)data;
  fill_mac_ind_data(mac);
  return true;
}

void read_mac_setup_sm(void* data)
{
  assert(data != NULL);
//  assert(data->type == MAC_AGENT_IF_E2_SETUP_ANS_V0 );

  assert(0 !=0 && "Not supported");
}

sm_ag_if_ans_t write_ctrl_mac_sm(void const* data)
{
  assert(data != NULL);

  mac_ctrl_req_data_t* ctrl = (mac_ctrl_req_data_t*)data; 
  assert(ctrl->hdr.dummy == 1);
  assert(ctrl->msg.action == 42);

  sm_ag_if_ans_t ans = {.type = CTRL_OUTCOME_SM_AG_IF_ANS_V0 };
  return ans;
}

