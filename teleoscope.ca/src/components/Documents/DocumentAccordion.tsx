import * as React from 'react';
import { styled } from '@mui/material/styles';
import ArrowForwardIosSharpIcon from '@mui/icons-material/ArrowForwardIosSharp';
import MuiAccordion, { AccordionProps } from '@mui/material/Accordion';
import MuiAccordionSummary, {
  AccordionSummaryProps,
} from '@mui/material/AccordionSummary';
import MuiAccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import DocumentList from './DocumentList';
import { Doclist, Graph } from '@/types/graph';

const Accordion = styled((props: AccordionProps) => (
  <MuiAccordion disableGutters elevation={0} square {...props} />
))(({ theme }) => ({
  border: `1px solid ${theme.palette.divider}`,
  '&:not(:last-child)': {
    borderBottom: 0,
  },
  '&:before': {
    display: 'none',
  },
}));

const AccordionSummary = styled((props: AccordionSummaryProps) => (
  <MuiAccordionSummary
    expandIcon={<ArrowForwardIosSharpIcon sx={{ fontSize: '0.9rem' }} />}
    {...props}
  />
))(({ theme }) => ({
  backgroundColor:
    theme.palette.mode === 'dark'
      ? 'rgba(255, 255, 255, .05)'
      : 'rgba(0, 0, 0, .03)',
  flexDirection: 'row-reverse',
  '& .MuiAccordionSummary-expandIconWrapper.Mui-expanded': {
    transform: 'rotate(90deg)',
  },
  '& .MuiAccordionSummary-content': {
    marginLeft: theme.spacing(1),
  },
}));


const AccordionDetails = styled(MuiAccordionDetails)(({ theme }) => ({
  padding: theme.spacing(2),
  borderTop: '1px solid rgba(0, 0, 0, .125)',
}));

export default function DocumentAccordion({doclists, node}: {doclists: Array<Doclist>, node: Graph}) {
  const [expanded, setExpanded] = React.useState<string | false>("");

  const handleChange = (panel: string) => (event: React.SyntheticEvent, newExpanded: boolean) => {
      setExpanded(newExpanded ? panel : false);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
        {doclists?.map((doclist) => 
        <Accordion key={`${doclist.uid}-doclist`} style={{ flex: '1' }} expanded={expanded === doclist.uid} onChange={handleChange(doclist.uid)}>
          <AccordionSummary aria-controls="panel1d-content" id="panel1d-header">
          <Typography>{doclist.uid}</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <DocumentList data={doclist.ranked_documents} ></DocumentList>
          </AccordionDetails>
        </Accordion>
      )}</div>
  )
}